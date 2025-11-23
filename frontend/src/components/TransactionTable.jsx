// Make HTTP request to get transaction table data render during mounting stage. Render new rows at the top of the table. 

import TransactionTableRow from "./TransactionTableRow";

export default function TransactionTable () {
    return (
        <div className="transaction-table">
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Memo</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <TransactionTableRow/>
                </tbody>
            </table>
        </div>
    )
}