import click
import logging
from tabe import create_basic_app
from flask.cli import FlaskGroup
from .tabelog import TabelogSpider


def _create_app(_):
    app = create_basic_app()
    return app


@click.group(cls=FlaskGroup, create_app=_create_app)
def cli():
    format_ = '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'
    logging.basicConfig(format=format_, level=logging.INFO)


@cli.command()
def run():
    TabelogSpider().run()


if __name__ == '__main__':
    cli()