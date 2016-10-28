<?php
//проверяем значения полученые при проверке скриптом формы
if (trim($_POST['valTrFal'])!='valTrFal_true') {
	echo 'fasle';
}
else {

		$txtname = trim($_POST['txtname']);

		$txtNameValue = trim($_POST['name_class_value']);

		$txtemail = trim($_POST['txtemail']);

		$txtmessage = trim($_POST['txtmessage']);

		// от кого
		$fromMail = 'info@tester_mailerds.ru';
		$fromName = 'NameSendler';

		// Сюда введите Ваш email
		$emailTo = 'a.v.malashina@gmail.com';

		$subject = 'Форма обратной связи';
		$subject = '=?utf-8?b?'. base64_encode($subject) .'?=';
		$headers = "Content-type: text/plain; charset=\"utf-8\"\r\n";
		$headers .= "From: ". $fromName ." <". $fromMail ."> \r\n";

		// тело письма
		$body = "Получено письмо с сайта MRD.com\n\nИмя: $txtname\ne-mail: $txtemail \nСообщение: $txtmessage";
		$mail = mail($emailTo, $subject, $body, $headers, '-f'. $fromMail );


		echo 'ok';
}
?>
