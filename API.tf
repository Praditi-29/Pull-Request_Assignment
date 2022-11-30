
resource "local_file" "String-Variable" {
content = "Creating CSS File."
filename = var.String-Type
}

resource "local_file" "Number-Variable" {
content = var.Number-Type
filename = "NumberVariable.js"
}

resource "local_file" "List-String-Variable" {
content = var.List-Type-String[1]
filename = "ListVariableStringOnly.json"
}

resource "local_file" "List-Any-Variable" {
content = var.List-Type-Any[2]
filename = "ListVariableAny.txt"
}

resource "local_file" "Map-Variable" {
content = var.Map-Type["content"]
filename = var.Map-Type["filename"]
}

resource "local_file" "Object-Variable" {
content = var.Object-Type.name
filename ="ObjectVariable.html"
}
