import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))
    
    @classmethod
    def resolve_hello(self, info, argument):
        return 'Hello ' + argument
