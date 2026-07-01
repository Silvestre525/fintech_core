from sqlalchemy import String, Numeric, DateTime, func, Enum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid
from decimal import Decimal
from app.core.settings import Base
from app.wallets.enums import WalletStatus

class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=Decimal("0.00"), index=True, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="ARS", nullable=False)
    status: Mapped[WalletStatus] = mapped_column(Enum(WalletStatus), default=WalletStatus.ACTIVE, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
