{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "13dd564e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Resources\\budget_data.csv\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Resources\\\\budget_data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_3596/1554889405.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mbudgetdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[1;31m#read csv file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 19\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbudgetdata\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mcsvfile\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     20\u001b[0m     \u001b[0mcsvreader\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcsv\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvfile\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdelimeter\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m','\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     21\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvreader\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mnone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Resources\\\\budget_data.csv'"
     ]
    }
   ],
   "source": [
    "#modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#trackers\n",
    "totalmonths = 0\n",
    "totalrev = 0\n",
    "pastrev = 0\n",
    "highestrev = 0\n",
    "lowestrev = 0\n",
    "\n",
    "#create revenue bucket\n",
    "revchange = []\n",
    "\n",
    "#link data\n",
    "path=\"Resources\\\\budget_data.csv\"\n",
    "budgetdata = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "print (budgetdata)\n",
    "#read csv file\n",
    "with open(budgetdata) as csvfile:\n",
    "    csvreader=csv.reader(csvfile,delimeter=',')\n",
    "    print(csvreader,none)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2471e284",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
