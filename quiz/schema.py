import graphene
from graphene_django import DjangoObjectType
from book.models import Books
from .models import *


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class CategoryType(DjangoObjectType):
    class Meta:
        model = QuizCategory
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_books(root, info):
        return Books.objects.filter(title="django")

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID
        name = graphene.String(required=True)
        category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = QuizCategory.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


# class CategoryMutation(graphene.Mutation):
# class Arguments:
#    id = graphene.ID
#   category = graphene.Field(CategoryType)

# @classmethod
# def mutate(cls, root, info,  id):
#    category = QuizCategory.objects.get(id=id)
#  category.delete()
# return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
