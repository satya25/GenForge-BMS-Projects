 
# Component: Search & Filter Utilities

## Overview
The Search & Filter Utilities module provides a common framework for querying, filtering, and retrieving data across all projects. It ensures consistent search behavior, efficient performance, and user-friendly interfaces for both simple and advanced queries.

## Features
- **Keyword Search**: Basic text search across records.
- **Field-Based Filtering**: Filter by attributes (e.g., date, status, category).
- **Pagination & Sorting**: Support for large datasets with ordered results.
- **Advanced Queries**: Combine multiple filters with AND/OR logic.
- **Role-Based Access**: Restrict search results based on user permissions.
- **Audit Logging**: Record search queries for monitoring and optimization.

## Architecture
- **Core Components**:
  - Query Builder (constructs SQL queries safely)
  - Filter Processor (applies conditions dynamically)
  - Result Formatter (standardizes output in JSON/array)
- **Dependencies**:
  - PHP CRUD Classes (for database access)
  - Configuration Manager (default limits, sorting rules)
  - Event Logger (to record search activity)
- **Interfaces**:
  - REST API endpoints (`/search`, `/filter`)
  - PHP/Python utility classes for internal use

---

## Usage Guidelines
- **Consistency**:
  - All projects must use this shared utility for search/filter operations.
  - No inline SQL queries allowed — always use Query Builder.
- **Security**:
  - Sanitize all user inputs before building queries.
  - Enforce role-based access control to prevent unauthorized data exposure.
- **Performance**:
  - Use pagination for large datasets.
  - Apply indexes on frequently searched fields.
- **Error Handling**:
  - Return descriptive error messages for invalid filters.
  - Log failed queries for debugging.

---

## Example: PHP (Search with PDO)
```php
try {
    $pdo->beginTransaction();

    $stmt = $pdo->prepare("SELECT id, name, status FROM projects WHERE status = :status ORDER BY name LIMIT 10");
    $stmt->execute([':status' => $status]);
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    $pdo->commit();
    echo json_encode($results);
} catch (Exception $e) {
    $pdo->rollBack();
    $eventLogger->error("Search error: " . $e->getMessage());
}
```

---

## Example: Python (FastAPI + SQLAlchemy)
```python
from fastapi import FastAPI, Query
from sqlalchemy.orm import Session
from models import Project

app = FastAPI()

@app.get("/projects/")
def search_projects(status: str = Query(None), db: Session = Depends(get_db)):
    try:
        query = db.query(Project)
        if status:
            query = query.filter(Project.status == status)
        results = query.order_by(Project.name).limit(10).all()
        return results
    except Exception as e:
        return {"error": str(e)}
```

---

## Best Practices
- Always use prepared statements or ORM filters.
- Provide default sorting (e.g., by name or date).
- Limit results to prevent overload (e.g., max 100 records).
- Document available filters in API docs.
- Regularly review query performance with indexes.

---

## Future Enhancements
- Full-text search support.
- Faceted search for multi-dimensional filtering.
- Search suggestions/autocomplete.
- Integration with external search engines (Elasticsearch, Solr).
  
---
 