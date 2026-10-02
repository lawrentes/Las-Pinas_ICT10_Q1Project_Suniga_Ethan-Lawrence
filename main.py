from pyscript import document

def SKU_generator(event):
    brand = document.getElementById("brand").value
    product_type = document.getElementById("type").value
    color = document.getElementById("color").value

    sku = f"{brand}-{product_type}-{color}"
    document.getElementById("sku-display").innerText = sku

# ms. i give up