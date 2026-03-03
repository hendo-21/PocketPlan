// Make HTTP request to get transaction table data render during mounting stage. Render new rows at the top of the table. 

import TransactionTableRow from "./TransactionTableRow";

export default function TransactionTable ({ transactions, isEditing, setIsEditing, onEdit, onDelete }) {
    return (
        <div className="transaction-table">
            <h4>Your Spending</h4>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Memo</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    { transactions.map((transactions, i) => 
                        <TransactionTableRow 
                            transaction={transactions} 
                            key={i} 
                            isEditing={isEditing} 
                            setIsEditing={setIsEditing}
                            onDelete={onDelete} 
                            onEdit={onEdit}
                        />
                    ) }
                </tbody>
            </table>
        </div>
    )
}