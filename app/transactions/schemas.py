from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from uuid import UUID
from datetime import datetime
from app.transactions.enums import TransactionStatus

class TransactionCreate(BaseModel):
    amount: Decimal
    target_wallet_id: uuid.UUID


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    amount: Decimal
    target_wallet_id: uuid.UUID    
    source_wallet_id: uuid.UUID
    status: TransactionStatus

    created_at: datetime

