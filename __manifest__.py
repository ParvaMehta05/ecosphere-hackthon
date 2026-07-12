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
<<<<<<< HEAD
        'security/ir.model.access.csv', 
        'views/menu.xml',
        'views/environmental_view.xml',
        'views/governance_view.xml',
        'views/gamification_view.xml',
        'views/social_view.xml' 
       
=======
        'security/ir.model.access.csv',  
        # 'views/organization_vieAws.xml',  # Placeholders for Phase 4 UI work
>>>>>>> 149996e3785aef2a90d0d5b9e108df89f1a24d7a
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}