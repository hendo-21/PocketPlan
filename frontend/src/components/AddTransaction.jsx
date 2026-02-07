import { useState } from "react"
import { MdClose } from "react-icons/md"

export default function AddTransaction({ setIsAdding, loadTotalSpent, loadTransactions }) {
    // Prepare state
    const [date, setDate] = useState("");
    const [amount, setAmount] = useState(0.0);
    const [memo, setMemo] = useState("");

    // Add new transaction to Transactions table in db
    const createTransaction = async () => {
        const newTransaction = { date, amount, memo };
        const response = await fetch('/api/transactions', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(newTransaction)
        });
        if(response.status !== 201) {
            alert(`Could not add transaction due to error: ${response.status}`);
            }
        }

    return (
        <>
            <form className="add-transaction-form" onSubmit={ async (e) => {
                e.preventDefault();
                await createTransaction();
                await loadTransactions();
                setIsAdding(false);
                loadTotalSpent();
                }}>

                <div className="add-transaction-header">
                    <h4>Add Transaction</h4>
                    <MdClose onClick={() => setIsAdding(false)}/>
                </div>

                <p>
                    <label> Date
                        <input type="date" id="date" name="date" value={date} required
                        onChange={ e => { setDate(e.target.value) } }></input>
                    </label>
                </p>

                <p>
                    <label> Amount
                        <input type="number" id="amount" name="amount" step="0.01" placeholder="0.00" value={amount}
                        onChange={ e => { setAmount(e.target.valueAsNumber) } }></input>
                    </label>
                </p>

                <p>
                    <label> Memo
                        <input type="text" id="memo" name="memo" placeholder="Brief description" value ={memo}
                        onChange={ e => { setMemo(e.target.value) } }></input>
                    </label>
                </p>

                <button type="submit">
                    Add
                </button>

            </form>
        </>
    )
}