def count_def(carts):
    total_amount,total_quantity= 0,0
    if carts:
        for c in carts.values():
            total_amount += c['amount']
            total_quantity += c['quantity']
        return {
            'total_amount':total_amount,
            'total_quantity':total_quantity
        }