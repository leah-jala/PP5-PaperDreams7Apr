from django import template
import json

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='get_item_qty')
def get_item_qty(bag, item_id):
    if isinstance(bag, str):
        if bag.strip() == "":
            bag = {}
        else:
            bag = json.loads(bag)
    return bag.get(str(item_id), 0)
