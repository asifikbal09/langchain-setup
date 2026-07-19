from typing import TypedDict

class ProductReview(TypedDict):
    product_name: str
    rating: int
    review: str

new_review : ProductReview ={
    "product_name": "Wireless Headphones",
    "rating": 5,
    "review": "These are amazing! I love them."
}

the_2nd_review : ProductReview = {
    "product_name": "Wireless Headphones",
    "rating": "4",
    "review": "Good sound quality, but a bit pricey."
}


print(new_review)
print(the_2nd_review)