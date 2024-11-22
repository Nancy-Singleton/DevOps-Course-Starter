```mermaid
C4Component
    Container(flask, "Flask Web Server")

    Container_Boundary(todoAppCode, "To-Do Application Code") {
        Component(htmlTemplates, "HTML Templates")
        Component(routes, "Webserver Routes", "app.py")
        Component(dataClasses, "Data Classes")
        Component(mongoDbClient, "MongoDB Client", "items_repository.py")
    }

    System_Ext(mongoDb, "Mongo DB")

    Rel(flask, routes, "Passes request to")

    Rel(htmlTemplates, routes, "")
    Rel(dataClasses, routes, "")
    Rel(dataClasses, mongoDbClient, "")
    Rel(routes, mongoDbClient, "")

    Rel(mongoDbClient, mongoDb, "Talks via HTTP")

    UpdateLayoutConfig($c4ShapeInRow="3")
    UpdateRelStyle(flask, routes, $offsetX="-175", $offsetY="-50")
    UpdateRelStyle(mongoDbClient, mongoDb, $offsetX="85", $offsetY="-150")
```