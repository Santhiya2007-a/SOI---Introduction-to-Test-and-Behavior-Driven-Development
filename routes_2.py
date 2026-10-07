@app.route("/products/<int:product_id>", methods=["DELETE"])

def delete_products(product_id):

    """Delete a Product"""



    product = Product.find(product_id)



    if product:

        product.delete()



    return "", status.HTTP_204_NO_CONTENT