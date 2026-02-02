 
# Component: PHP CRUD Classes

## Overview
The PHP CRUD Classes module provides a standardized way to perform Create, Read, Update, and Delete operations on MySQL databases. To ensure reliability, consistency, and security, **all queries — even single statements — must be wrapped inside PDO transactions and enclosed in `try...catch` blocks**.

## Features
- **Unified CRUD Operations**: Standardized methods for insert, select, update, and delete.
- **Transaction Safety**: Every query runs inside a PDO transaction, ensuring atomicity.
- **Error Handling**: All operations wrapped in `try...catch` to gracefully handle exceptions.
- **Prepared Statements**: Prevent SQL injection by using bound parameters.
- **Reusability**: Shared classes across all projects for consistent database access.
- **Logging**: Integration with Event Logger for query success/failure tracking.

## Architecture
- **Core Components**:
  - `Database.php` → PDO connection handler
  - `Crud.php` → Class with methods: `create()`, `read()`, `update()`, `delete()`
- **Dependencies**:
  - Configuration Manager (for DB credentials)
  - Event Logger (to record query execution and errors)
- **Interfaces**:
  - PHP classes callable from project modules
  - REST API endpoints that internally use CRUD classes

## Usage Guidelines
- **Transactions**:
  - Always start with `$pdo->beginTransaction()`.
  - Commit with `$pdo->commit()` if successful.
  - Rollback with `$pdo->rollBack()` on failure.
- **Error Handling**:
  - Wrap all queries in `try...catch`.
  - Log exceptions using Event Logger.
- **Prepared Statements**:
  - Use `$stmt = $pdo->prepare("...")` with bound parameters.
  - Never concatenate user input directly into SQL.
- **Consistency**:
  - All projects must use these shared CRUD classes.
  - No direct inline SQL queries allowed in project code.

## Example Implementation
```php
try {
    $pdo->beginTransaction();

    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    $stmt->execute([
        ':name' => $name,
        ':email' => $email
    ]);

    $pdo->commit();
    // Log success
    $eventLogger->info("User inserted successfully: $name");
} catch (Exception $e) {
    $pdo->rollBack();
    // Log failure
    $eventLogger->error("Database error: " . $e->getMessage());
}
```

## Best Practices
- Centralize DB credentials in the Configuration Manager.
- Always validate input before binding parameters.
- Keep CRUD methods generic and reusable.
- Ensure rollback is always called on failure.
- Use descriptive log messages for traceability.

## Future Enhancements
- Support for batch operations with transaction safety.
- Integration with ORM frameworks for advanced use cases.
- Automated unit tests for CRUD methods.
- Connection pooling for performance optimization.
 
--- 