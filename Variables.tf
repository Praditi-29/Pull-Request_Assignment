variable "String-Type" {
    type = string
    description = "It is a String Variable For creating files."
    default = "CSS-file.css"
}


variable "Number-Type" {
    type = number
    description = "It is Number Variable."
    default = 611
}

variable "List-Type-String" {
    type = list(string)
    description = "List Variable Of String Type"
    default = ["Apple","Banana","Cherry","Blossoms"]
}

variable "List-Type-Any" {
    type= list(any)
    description = "List Variable Of Any Type "
    default = ["Praditi",21,"Btech. Cse","Punjabi University"]
}

variable "Map-Type" {
    type = map(any)
    description = "Map Variable "
    default = { "filename" :"Types_Cloud.js"
    "content"="There are four main types of cloud computing: private clouds, public clouds, hybrid clouds, and multiclouds."
    }
}

variable "Object-Type" {
    type = object({
        name:string
        age:number
    })

    description = "Object Variable"
    default = {
      age = 21
      name = "Default-Name"
    }

}

