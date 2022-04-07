{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7725c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#trackers\n",
    "totalmonths = 0\n",
    "totalrev = 0\n",
    "pastrev =0\n",
    "highestrev = 0\n",
    "lowestrev = 0\n",
    "\n",
    "#create revenue bucket\n",
    "revchange = []\n",
    "\n",
    "#link data\n",
    "budgetdata=os.path.join('..', 'Resources', 'budget_data.csv')\n",
    "\n",
    "#read csv file\n",
    "with open(budgetdata) as csvfile:\n",
    "    csvreader=csv.reader(csvfile,delimeter=',')\n",
    "    print(csvreader,none)\n",
    "    "
   ]
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
