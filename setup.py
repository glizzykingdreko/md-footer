from setuptools import setup, find_packages

setup(
    name='md_footer',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'md-footer=md_footer:MDFooter',
        ]
    },
    author='GlizzyKingDreko',
    author_email='glizzykingdreko@protonmail.com',
    description="Manage and append consistent or dynamic footers to your Markdown files with md-footer, a versatile CLI tool.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/glizzykingdreko/md-footer',
    install_requires=[
    ],
    keywords=[
        'markdown', 
        'footer', 
        'documentation', 
        'markdown-footer', 
        'cli-tool', 
        'automation', 
        'md-footer', 
        'markdown-tool', 
        'append-footer', 
        'markdown-automation'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
