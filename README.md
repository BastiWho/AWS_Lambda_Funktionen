# READ ME Lambda Get / Post Methoden

## 1. Zwei Lambdafunktionen erstellen
### 1.1 Funktion Get (siehe Code "Lambda_Get_Function.py")
### 1.2 Funktion Post (siehe Code "Lambda_Post_Function.py")

## 2. API Gateway erstellen
### 2.1 Beide Lambdafunktionen im API Gateway verknüpfen
### 2.2 Get und Post Methode den entsprechenden Funktionen zuweisen

## 3. S3 Bucket erstellen

## 4. Berechtigungen innerhalb der Lambdafunktion vergeben
### 4.1 Lambda Post = `Put_object` für S3 Bucket als Berechtigung vergeben
### 4.2 Lambda Get = `Get_Object` für S3 Bucket als Berechtigung vergeben
### 4.3 Lambda Get = `Delete_Object` für S3 Bucket als Berechtigung vergeben

## 5. Test über z.B. Postman:

Mit dem Link aus dem API Gateway kann man nun im Postman einen Test starten. Unter POST sollte man mit dem Link nun eine Nachricht erstellen können. Diese sollte anschließend im S3 Bucket erscheinen. Als Rückgabewert kommt im Postman ein Link, welcher die Endung `.txt` hat.

Wenn man diesen Link nun als GET Methode aufruft, sollte man die Nachricht lesen können, und sie sollte aus dem S3 Bucket gelöscht werden.
