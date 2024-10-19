```mermaid
C4Context
    Person(user, "User")
    System_Ext(browser, "Web Browser")
    System(todoApp, "To-Do Application")
    System_Ext(mongoDb, "Mongo DB")

    Rel(user, browser, "Operates")
    Rel(browser, todoApp, "Talks via HTTP")
    Rel(todoApp, mongoDb, "Talks via HTTP")

    UpdateLayoutConfig($c4ShapeInRow="1")
    UpdateRelStyle(user, browser, $offsetX="5", $offsetY="0")
    UpdateRelStyle(browser, todoApp, $offsetX="5", $offsetY="0")
    UpdateRelStyle(todoApp, mongoDb, $offsetX="5", $offsetY="0")
```