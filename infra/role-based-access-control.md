 
# Component: Role-Based Access Control (RBAC)

## Overview
The RBAC module enforces fine-grained access control across all projects. It ensures that permissions are assigned based on roles, preventing unauthorized actions and maintaining system integrity. Roles can be hierarchical (e.g., Admin > Faculty > Student), with each role inheriting or restricting specific permissions.

## Features
- **Role Hierarchy**: Define roles such as Admin, Faculty, Student, and System.
- **Permission Mapping**: Associate roles with specific actions (CRUD, reporting, configuration).
- **Granular Access**: Control access at module, feature, and data levels.
- **Dynamic Assignment**: Allow role changes without code modifications.
- **Audit Trails**: Log role assignments, changes, and access attempts.
- **Integration**: Works seamlessly with User Management, Session Management, and REST API Services.

## Architecture
- **Core Components**:
  - Role Table (stores roles and hierarchy)
  - Permission Table (maps roles to actions/resources)
  - Access Control Middleware (enforces checks at runtime)
- **Dependencies**:
  - User Management (authentication)
  - Event Logger (audit trails)
  - Configuration Manager (role definitions)
- **Interfaces**:
  - PHP: Middleware functions checking role permissions
  - Python: Decorators for endpoint protection

---

## Usage Guidelines
- **Consistency**:
  - All projects must use RBAC for access control.
  - No hardcoded role checks in project code — always use shared middleware.
- **Security**:
  - Restrict sensitive operations (e.g., configuration changes) to Admin role.
  - Enforce least privilege principle — users only get the permissions they need.
- **Error Handling**:
  - Unauthorized access attempts must return HTTP 403 Forbidden.
  - Log all failed access attempts in Event Logger.
- **Best Practices**:
  - Keep role definitions centralized.
  - Regularly review and update permissions.
  - Provide clear documentation of role capabilities.

---

## Example: PHP (Middleware for RBAC)
```php
function checkAccess($requiredRole) {
    $userRole = $_SESSION['role'];
    if ($userRole !== $requiredRole) {
        $eventLogger->warn("Unauthorized access attempt by role: $userRole");
        http_response_code(403);
        echo json_encode(["error" => "Forbidden"]);
        exit();
    }
}
```

---

## Example: Python (FastAPI Decorator for RBAC)
```python
from fastapi import Depends, HTTPException

def role_required(required_role: str):
    def wrapper(user=Depends(get_current_user)):
        if user.role != required_role:
            # Log unauthorized attempt
            print(f"Unauthorized access attempt by role: {user.role}")
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return wrapper

@app.get("/admin-dashboard")
def admin_dashboard(user=Depends(role_required("Admin"))):
    return {"message": "Welcome to the Admin Dashboard"}
```

---

## Best Practices
- Define roles and permissions in configuration files or database tables.
- Use middleware/decorators for enforcement, not inline checks.
- Apply RBAC consistently across APIs, dashboards, and file storage.
- Regularly audit role assignments for compliance.

---

## Future Enhancements
- Attribute-Based Access Control (ABAC) for more flexible policies.
- Role inheritance (e.g., Faculty inherits Student permissions).
- Self-service role requests with admin approval.
- Integration with institutional identity providers for centralized RBAC.

