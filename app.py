import os
import secrets
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax', MAX_CONTENT_LENGTH=16384)
CENT = Decimal('0.01')


def money(value):
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


@app.template_filter('inr')
def inr(value):
    return f'₹{money(value):,.2f}'


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'csrf' not in session:
        session['csrf'] = secrets.token_hex(24)
    cart = session.get('cart', [])
    if request.method == 'POST':
        if not secrets.compare_digest(request.form.get('csrf', ''), session['csrf']):
            abort(400)
        action = request.form.get('action')
        if action == 'clear':
            session['cart'] = []
            flash('Cart cleared successfully.')
        elif action == 'add':
            name = request.form.get('name', '').strip()
            try:
                quantity = int(request.form.get('quantity', ''))
                price = Decimal(request.form.get('price', ''))
                if not name or len(name) > 40:
                    raise ValueError('Enter an item name with 1–40 characters.')
                if not 1 <= quantity <= 10000:
                    raise ValueError('Quantity must be a whole number from 1 to 10,000.')
                if not price.is_finite() or not Decimal('0.01') <= price <= Decimal('1000000'):
                    raise ValueError('Price must be between ₹0.01 and ₹1,000,000.')
                if len(cart) >= 20:
                    raise ValueError('You can add up to 20 items per bill.')
                cart.append({'name': name, 'quantity': quantity, 'price': str(money(price))})
                session['cart'] = cart
                flash(f'{name} added successfully.')
            except (InvalidOperation, ValueError) as error:
                flash(str(error) if isinstance(error, ValueError) and str(error).startswith(('Enter', 'Quantity', 'Price', 'You')) else 'Enter a valid quantity and price.')
        else:
            abort(400)
        return redirect(url_for('index'))
    items = [dict(item, total=money(item['price']) * item['quantity']) for item in cart]
    subtotal = sum((item['total'] for item in items), Decimal('0'))
    rate = 0 if subtotal < 500 else 5 if subtotal < 1000 else 10
    discount = money(subtotal * rate / 100)
    return render_template('index.html', items=items, subtotal=subtotal, rate=rate,
                           discount=discount, grand_total=subtotal - discount,
                           date=datetime.now().strftime('%d-%m-%Y'))


@app.get('/health')
def health():
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
