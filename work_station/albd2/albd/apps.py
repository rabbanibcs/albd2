from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('Article', children=[
            ChildItem(model='albd.categories'),
            ChildItem(model='albd.authors'),
            ChildItem(model='albd.content_types'),
            ChildItem(model='albd.positions')
        ], icon='fa fa-leaf'),
        # ParentItem('Integrations', children=[
        #     ChildItem(model='demo.city'),
        # ]),
        ParentItem('Users', children=[
            ChildItem(model='auth.user'),
            ChildItem('User groups', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Right Side Menu', children=[
            ChildItem('Password change', url='admin:password_change'),
            ChildItem('Open Google', url='http://google.com', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )
