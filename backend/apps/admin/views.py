# -*- coding: utf-8 -*-
'''站点首页视图'''
from flask import render_template

from . import admin_app, app_name


@admin_app.route(r'/')
def view_index():
    return render_template(app_name + '/pages/index.htm.j2', page_id='view_index')

@admin_app.route(r'/auth/login')
def view_auth_login():
    return render_template(app_name + '/pages/master/auth-login.html', page_id='view-auth-login')

@admin_app.route(r'/auth/login_ad')
def view_auth_login_ad():
    return render_template(app_name + '/pages/master/index.html')

@admin_app.route(r'/auth/find_pwd')
def view_auth_find_pwd():
    return render_template(app_name + '/pages/master/auth-find_pwd.html')



@admin_app.route('/widgets')
def view_widgets():
    return render_template(app_name + '/pages/widgets.htm.j2', page_id='view_widgets')

@admin_app.route('/bootcom')
def view_bootcom():
    return render_template(app_name + '/pages/bootstrap-components.htm.j2', page_id='view_bootcom')

@admin_app.route('/cards')
def view_cards():
    return render_template(app_name + '/pages/cards.htm.j2', page_id='view_cards')

@admin_app.route('/charts')
def view_charts():
    return render_template(app_name + '/pages/charts.htm.j2', page_id='view_charts')

@admin_app.route('/form_fromcom')
def view_fromcom():
    return render_template(app_name + '/pages/form-components.htm.j2', page_id='view_fromcom')


@admin_app.route('/form_custom')
def view_custom():
    return render_template(app_name + '/pages/form_custom_elements.htm.j2', page_id='view_custom')

@admin_app.route('/form_sample')
def view_samples():
    return render_template(app_name + '/pages/form_samples.htm.j2', page_id='view_samples')

@admin_app.route('/form_notifications')
def view_notifications():
    return render_template(app_name + '/pages/form_notifications.htm.j2', page_id='view_notifications')
    

@admin_app.route('/table_basic')
def view_basic():
    return render_template(app_name + '/pages/table_basic.htm.j2', page_id='view_basic')


@admin_app.route('/table_data')
def view_data():
    return render_template(app_name + '/pages/table_data.htm.j2', page_id='view_data')



@admin_app.route('/page_blank')
def view_blank():
    return render_template(app_name + '/pages/page_blank.htm.j2', page_id='view_blank')

@admin_app.route('/page_calendar')
def view_calendar():
    return render_template(app_name + '/pages/page_calendar.htm.j2', page_id='view_calendar')

@admin_app.route('/page_invoice')
def view_invoice():
    return render_template(app_name + '/pages/page_invoice.htm.j2', page_id='view_invoice')

@admin_app.route('/page_mailbox')
def view_mailbox():
    return render_template(app_name + '/pages/page_mailbox.htm.j2', page_id='view_mailbox')

@admin_app.route('/page_error')
def view_error():
    return render_template(app_name + '/pages/page_error.htm.j2', page_id='view_error')

@admin_app.route('/page_user')
def view_user():
    return render_template(app_name + '/pages/page_user.htm.j2', page_id='view_user')
