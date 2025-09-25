```
Each __init__.py can be empty.
This tells Python: “yo, these are packages.”

```

#Injecting Dependencies in FastAPI

```

Dependency Injection is a software design pattern where objects (dependencies) are provided to a class or function instead of being instantiated inside it. This creates loose coupling, making your code easier to test, maintain, and scale.

```

1️⃣ Project Structure Overview

```
The project uses a layered architecture, which is a common best practice:

Controllers → handle API routes, HTTP requests/responses.

Services → contain business logic, the “what should happen” part.

Repositories → handle data access, like DB queries or API calls.

Models → define data schemas, usually with Pydantic.

```

#Think of it like this:

```

Client → Controller → Service → Repository → Database

```
