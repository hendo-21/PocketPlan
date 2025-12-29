import { MdOutlineEditNote } from "react-icons/md";
import { parseISO, format } from 'date-fns';

export default function TransactionTableRow({ transaction }) {
    // Convert date ISO to a Date object
    const dateObj = parseISO(transaction.date_added)

    // Format the Date object
    const formattedDate = format(dateObj, 'MM/dd/yy')

    return (
        <tr>
            <td>{formattedDate}</td>
            <td>${transaction.amount}</td>
            <td>{transaction.memo}</td>
            <td><MdOutlineEditNote/></td>
        </tr>
    )
}