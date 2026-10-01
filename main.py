from pyscript import display, document #WHY is it yellow WHYY is it NOT WOKING

def SKU_generator(e):
    
    document.getElementById('sku-display').innerHTML = " "

    
    
    category = document.getElementById('brand-select').value
    product_name = document.getElementById('type-select').value
    stock_qty = document.getElementById('quantity').value
    
    sku = str(category).upper() + "-" + str(product_name).upper() #i found this improved one on the internet
    #it might clip into the words
    display("SKU: ", sku, target='sku-display')


def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    

    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)
                
    tax_rate = 0.12  
    tax = subtotal * tax_rate
    total = subtotal + tax
    
# ty8s next one is from yoir code thank you :)
    receipt = f""" 
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """
    

    document.getElementById("show").innerHTML = receipt

