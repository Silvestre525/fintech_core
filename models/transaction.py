from sqlalchemy import Mapped, mapped_column, String, Numeric, DateTime, func, Enum, ForeignKey
import uuid
from datetime import datetime
from decimal import Decimal
from ..core.settings import Base
from ..enums.walletEnums import Status
from ..enums.transactionEnum import TransactionStatus


class Transaction(Base):
    __tablename__ = "Transaction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    source_wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("wallet.id"), nullable=False)
    target_wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("wallet.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12,2), nullable=False)
    status: Mapped[TransactionStatus] = mapped_column(Enum(TransactionStatus), default=TransactionStatus.PENDING)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
