# Fasten

The fasten CLI tool is a convention based devtool which helps speed up initialising and developing CRUD architecture for FastAPI projects. Taking inspiration from `rails generate` commands, fasten aims to provide a route->service->repository approach common to MVC applications. By using this convention, fasten does the heavy lifting of setting up files for each model you work with, providing an extensible starting point so you can focus on logic, not boilerplate.

## Commands (WIP)

`fasten init` - Generate a new project

```
src/
├── routes/
│   └── dependencies.py
├── services/
├── repos/
│   └── base.py
├── utils/
│   └── types.py
└── main.py
```

`fasten generate NAME --fields f1:int f2:str f3:list[str]` - Creates a new CRUD stack for NAME - Add new repo class which extends base.py - Add new service which calls the repo - Add new route which returns the response from service using response_type

## fasten.yaml

```yaml
fasten:
    version: "1.0"
    async: true # Make function calls async
    # other options to be added
```
