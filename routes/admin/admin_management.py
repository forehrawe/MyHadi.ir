from flask import Blueprint, render_template
from routes.admin.check_permission import check_permission



admin_mgmt_page_bp = Blueprint('admin_mgmt', __name__)



                

@admin_mgmt_page_bp.route('/admin_management')
def admin_mgmt():
    
    if not check_permission():
        return render_template('admin/errPerm.html')
        
    
    
    return render_template('admin/admin_management.html')