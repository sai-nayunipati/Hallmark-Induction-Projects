// totalPrice is a NEW variable initialized to ZERO, product is the element
products.reduce((totalPrice, product)=> {
    totalPrice += product.price
}, 0)

console.log(totalPrice)