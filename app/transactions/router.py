from fastapi import APIRouter, Depends
from schemas import TransactionResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Transaction

router = APIRouter(prefix="/transaction", tags=["Transactions"])


@router.get('/', response_model=list[TransactionResponse])
async def get_transaction(limit: int = 20, offset: int = 0, db: AsyncSession=Depends(get_db)):
    qs = select(Transaction).limit(limit).offset(offset)

    result = await db.execute(qs)

    transactions = result.scalars().all()

    return transactions