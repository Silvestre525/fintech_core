from sqlalchemy import Mapped, mapped_column, String, Numeric
from sqlalchemy import Enum
import uuid
from ..core.settings import Base
from ..enums.walletEnums import Status

class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    balance: Mapped[float] = mapped_column(Numeric(12, 2),default=0.00 , index=True, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="ARS", nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.ACTIVE, nullable=False)
