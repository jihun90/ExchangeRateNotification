import json
import defCommon
import requests
from typing import List, Set, Dict, Tuple
from datetime import datetime


def getTodayDate() -> str:
    return datetime.now().date().__str__()


def getExchangeRateData(param: dict) -> dict:
    return requests.get(defCommon.EXCHANGE_API_URL, param)


def main():
    with open(defCommon.PARAM_PATH) as file:
        param: Dict[str, str, str] = json.load(file)

    param["searchdate"] = "2023-01-01"  # getTodayDate()
    param["data"] = defCommon.DATA_PARAM

    exchangeRateData: dict = getExchangeRateData(param).json()

    if exchangeRateData is None:
        exit()

    if len(exchangeRateData) > 0:
        exit()

    if exchangeRateData == defCommon.RESULT_PARAM_SUCESS:
        print(exchangeRateData)


if __name__ == "__main__":
    main()
