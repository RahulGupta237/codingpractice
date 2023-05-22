class Kellton:
    project_name="Abbott"
    def __init__(self,name) -> None:
        
        self.name=name
print(Kellton.project_name)
s=Kellton("Sandeep")
print(s.name)