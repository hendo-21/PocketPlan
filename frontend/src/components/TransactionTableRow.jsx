import { MdOutlineEditNote, MdDeleteOutline } from "react-icons/md";
import { parseISO, format } from 'date-fns';

import EditTransaction from "./EditTransaction";

export default function TransactionTableRow({ transaction, isEditing, setIsEditing, onDelete, onEdit }) {
    // Convert date ISO to a Date object
    const dateObj = parseISO(transaction.date_added);

    // Format the Date object
    const formattedDate = format(dateObj, 'MM/dd/yy');

    return (
        <>
            <tr>
                <td>{formattedDate}</td>
                <td>${(transaction.amount).toFixed(2)}</td>
                <td>{transaction.memo}</td>
                <td className='action-icons'><MdOutlineEditNote onClick={() => setIsEditing(transaction.id)}/></td>
                <td className='action-icons'><MdDeleteOutline onClick={() => onDelete(transaction.id)}/></td>
            </tr>
            {isEditing === transaction.id && (
                <tr>
                    <td colSpan={5}><EditTransaction transaction={transaction} onEdit={onEdit} setIsEditing={setIsEditing}/></td>
                </tr>
            )}
        </>
    )
}