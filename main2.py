from pyscript import document

def create_order(event):
    subtotal = 0
    for i in range(1, 6): 
        item = document.getElementById(f"item{i}")
        if item.checked:
            subtotal += float(item.value)

    tax = subtotal * 0.12
    total = subtotal + tax

    document.getElementById("show").innerHTML = f"""
        <h3>==== Receipt ====</h3>
        <p>Subtotal: ₱{subtotal:.2f}</p>
        <p>Tax: ₱{tax:.2f}</p>
        <p><strong>Total: ₱{total:.2f}</strong></p>
    """