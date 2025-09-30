"""enums changed for types in database and architecture models

Revision ID: 17a9183d0b31
Revises: 8ae3328f1608
Create Date: 2025-09-30 19:43:21.146351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "17a9183d0b31"
down_revision: Union[str, Sequence[str], None] = "8ae3328f1608"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: change enums to string types."""
    op.alter_column(
        "architecture",
        "type",
        existing_type=sa.String(),  # usamos String directamente
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "database",
        "name",
        existing_type=sa.String(),
        type_=sa.String(),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema: revert to original enum-like string types."""
    # ⚠️ Nota: al haber eliminado los ENUM, el downgrade aquí
    # vuelve a String porque no tenemos ya los Enum definidos en SQLModel.
    # Si quisieras restaurarlos, tendrías que recrear los ENUMs manualmente.
    op.alter_column(
        "database",
        "name",
        existing_type=sa.String(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "architecture",
        "type",
        existing_type=sa.String(),
        type_=sa.String(),
        existing_nullable=False,
    )
