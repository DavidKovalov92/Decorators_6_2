def is_admin(func, **kwargs):
    def wrapper(**kwargs):
        if func(**kwargs) == 'admin':
            print('Permission success')
        elif func(**kwargs) == 'user':
            raise ValueError('Permission denied')
        return func(**kwargs)
    return wrapper



@is_admin
def show_customer_receipt(user_type: str):
    return user_type

show_customer_receipt(user_type='admin')