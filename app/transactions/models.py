from sqlalchemy import Numeric, DateTime, func, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime
from decimal import Decimal
from app.core.settings import Base
from app.transactions.enums import TransactionStatus

class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    source_wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("wallet.id"), nullable=False)
    target_wallet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("wallet.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[TransactionStatus] = mapped_column(Enum(TransactionStatus), default=TransactionStatus.PENDING)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
