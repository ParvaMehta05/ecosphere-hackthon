{
    'name': 'EcoSphere: ESG Management Platform',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Manage Environmental, Social, and Governance performance',
    'description': """
        EcoSphere ESG Management Platform
        =================================
        A centralized application to track carbon emissions, promote employee participation 
        through gamification, and maintain governance compliance.
    """,
    'author': 'PM',
    'depends': ['base', 'mail'], 
    'data': [
        'security/ir.model.access.csv',  
        # 'views/organization_views.xml',  # Placeholders for Phase 4 UI work
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}