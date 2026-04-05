import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Basil's Coffee Shop PRO</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: linear-gradient(to right, #3e2c23, #b08968);
    color: white;
    text-align: center;
}

h1 {
    padding: 20px;
}

.menu {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    padding: 20px;
}

.item {
    background: white;
    color: black;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    transition: transform 0.2s;
}

.item:hover {
    transform: scale(1.05);
}

img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

button {
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #6f4e37;
    color: white;
    border-radius: 10px;
    cursor: pointer;
}

button:hover {
    background: #4b2e2e;
}

.cart {
    position: fixed;
    right: 20px;
    top: 20px;
    background: white;
    color: black;
    padding: 15px;
    border-radius: 15px;
    width: 220px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
}

.cart h3 {
    margin-top: 0;
}

.cart button {
    width: 100%;
    margin-top: 10px;
}

.checkout {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.8);
    justify-content: center;
    align-items: center;
}

.checkout-box {
    background: white;
    color: black;
    padding: 30px;
    border-radius: 15px;
    width: 300px;
}
</style>
</head>

<body>

<h1>☕ Basil's Coffee Shop PRO</h1>

<div class="cart">
    <h3>🛒 Cart</h3>
    <div id="cartItems">Empty</div>
    <p><b>Total:</b> <span id="total">0</span> SAR</p>
    <button onclick="openCheckout()">Checkout</button>
</div>

<div class="menu">

<div class="item">
<img src="https://placehold.co/300x200?text=Espresso">
<h3>Espresso</h3>
<p>10 SAR</p>
<button onclick="addItem('Espresso',10)">Add</button>
</div>

<div class="item">
<img src="https://placehold.co/300x200?text=Hot+Chocolate">
<h3>Hot Chocolate</h3>
<p>12 SAR</p>
<button onclick="addItem('Hot Chocolate',12)">Add</button>
</div>

<div class="item">
<img src="https://placehold.co/300x200?text=Spanish+Latte">
<h3>Spanish Latte</h3>
<p>14 SAR</p>
<button onclick="addItem('Spanish Latte',14)">Add</button>
</div>

<div class="item">
<img src="https://placehold.co/300x200?text=Mocha">
<h3>Mocha</h3>
<p>13 SAR</p>
<button onclick="addItem('Mocha',13)">Add</button>
</div>

<div class="item">
<img src="https://placehold.co/300x200?text=Cappuccino">
<h3>Cappuccino</h3>
<p>13 SAR</p>
<button onclick="addItem('Cappuccino',13)">Add</button>
</div>

<div class="item">
<img src="https://placehold.co/300x200?text=Iced+Coffee">
<h3>Iced Coffee</h3>
<p>11 SAR</p>
<button onclick="addItem('Iced Coffee',11)">Add</button>
</div>

</div>

<div class="checkout" id="checkout">
  <div class="checkout-box">
    <h2>💳 Checkout</h2>
    <p>Enter your name:</p>
    <input id="name" placeholder="Your Name" style="padding:10px;width:90%;">
    <br><br>
    <button onclick="pay()">Pay Now</button>
    <button onclick="closeCheckout()">Cancel</button>
  </div>
</div>

<script>
let cart = [];

function addItem(name, price) {
    cart.push({name, price});
    updateCart();
}

function updateCart() {
    let cartDiv = document.getElementById("cartItems");
    let total = 0;

    if (cart.length === 0) {
        cartDiv.innerHTML = "Empty";
    } else {
        cartDiv.innerHTML = "";
        cart.forEach((item, index) => {
            total += item.price;
            cartDiv.innerHTML += `
                <div>
                    ${item.name} - ${item.price} SAR
                    <button onclick="removeItem(${index})">x</button>
                </div>
            `;
        });
    }

    document.getElementById("total").innerText = total;
}

function removeItem(i) {
    cart.splice(i, 1);
    updateCart();
}

function openCheckout() {
    document.getElementById("checkout").style.display = "flex";
}

function closeCheckout() {
    document.getElementById("checkout").style.display = "none";
}

function pay() {
    let name = document.getElementById("name").value;
    let total = document.getElementById("total").innerText;

    document.body.innerHTML = `
        <div style="padding:50px;">
            <h1>✅ Payment Successful!</h1>
            <h2>Thank you, ${name || "Customer"} ☕</h2>
            <p>Total Paid: ${total} SAR</p>
            <button onclick="location.reload()">Back to Shop</button>
        </div>
    `;
}
</script>

</body>
</html>
"""

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

httpd = HTTPServer(("localhost", PORT), Handler)

print(f"Running on http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

httpd.serve_forever()
