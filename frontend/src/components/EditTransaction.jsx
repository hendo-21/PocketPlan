import { useState } from "react";
import { MdClose } from "react-icons/md";

export default function EditTransaction ({ transaction, onEdit, setIsEditing }) {
    // Prepare state to store new user input
    const [date, setDate] = useState(transaction.date_added);
    const [amount, setAmount] = useState(transaction.amount);
    const [memo, setMemo] = useState(transaction.memo);

    return (
        <form className="edit-transaction-form" autoComplete="off" onSubmit={ async (e) => {
            e.preventDefault();
            onEdit(transaction.id, date, amount, memo);
            setIsEditing('');
        }}>
            <div className="edit-transaction-header">
                <h4>Edit Transaction</h4>
                <MdClose onClick={() => setIsEditing('')}/>
            </div>

            <p>
                <label> Date
                    <input type="date" id="date" name="date" value={date} required
                    onChange={ e => { setDate(e.target.value) } }></input>
                </label>
            </p>

            <p>
                <label> Amount
                    <input type="number" id="amount" name="amount" step="0.01" placeholder="0.00" value={amount} required
                    onChange={ e => { setAmount(e.target.valueAsNumber) } }></input>
                </label>
            </p>

            <p>
                <label> Memo
                    <input type="text" id="memo" name="memo" placeholder="Brief description" value ={memo} required
                    onChange={ e => { setMemo(e.target.value) } }></input>
                </label>
            </p>

            <button type="submit">
                Save
            </button>


        </form>
    )
}