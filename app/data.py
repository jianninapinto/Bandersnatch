from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    A Database class to manage a MongoDB database connection and functionality on a specific collection.

    This class uses the `load_dotenv()` function to load environment variables from a `.env` file. These environment
    variables are necessary to establish a connection to the database.

    :arg:
        database: The MongoDB database accessed through the `pymongo` package.
    """

    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        """
        Initialize the database object with a specific collection name.

        :arg:
            collection (str): The name of the collection to work with in the database.

        """
        self.collection = self.database[collection]

    def seed(self, amount: int) -> bool:
        """
        Insert any number of monsters into the collection using list comprehension, where a Monster object is
        generated as a dictionary using `to_dict()` for each value in the range from 1 to `amount + 1`. The resulting
        list of monster dictionaries is then inserted into the collection using the `insert_many()` method.

        :arg:
            amount (int): The number of monsters to insert.

        :return:
            bool: True if the insertion was acknowledged, False otherwise.
        """
        my_monsters = [Monster().to_dict() for _ in range(1, amount + 1)]
        result = self.collection.insert_many(my_monsters)
        return result.acknowledged

    def reset(self):
        """
        Delete all monsters from the collection using the `delete_many()` method. This operation removes all monsters
        (documents) that match the specified query, which in this case, is an empty dictionary.

        :return:
            bool: True if the deletion was acknowledged, False otherwise.
        """
        return self.collection.delete_many({})

    def count(self) -> int:
        """
        Calculate the number of monsters in the collection using the `count_documents()` method. By specifying an
        empty query ({}) in the method, all monsters (documents) are considered for counting.

        :return:
            int: The number of monsters in the collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Retrieve all monsters and their attributes from the collection using the `find()` method, which performs a
        query to retrieve the monsters (documents) from the collection. The results are converted into a list to
        gather all the records and then the list is transformed into a pandas DataFrame.

        :return:
            pandas.DataFrame: A DataFrame containing all the monsters and their respective attributes.
        """
        data = list(self.collection.find())
        return DataFrame(data)

    def html_table(self) -> str:
        """
        Retrieve the monsters' information from the pandas DataFrame as an HTML table string by using the `dataframe(
        )` method. The `to_html()` method is then applied to the DataFrame to convert it into an HTML table string
        that can be used in web applications.

        :return:
            str: The HTML table string representing the monsters' attributes information.
        """
        return self.dataframe().to_html()


if __name__ == '__main__':
    db = Database("monsters")
    db.reset()
    db.seed(1500)
    print(db.count())
    print(db.dataframe())
    print(db.html_table())
