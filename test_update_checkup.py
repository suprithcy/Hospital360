import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from io import StringIO
from Doctor_checkup import update_patient_checkup

class TestUpdatePatientCheckup(unittest.TestCase):

    @patch("builtins.input", side_effect=["P001", "Patient is stable"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("pandas.read_csv")
    @patch("os.path.exists", return_value=True)
    def test_valid_patient_update(self, mock_exists, mock_read_csv, mock_file, mock_input):
        df = pd.DataFrame({
            "Patient_ID": ["P001"],
            "Name": ["Alice"],
            "Symptoms": ["Fever"]
        })
        mock_read_csv.return_value = df

        with patch("sys.stdout", new=StringIO()):
            update_patient_checkup()

        # Check if file was written
        handle = mock_file()
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("Patient_ID: P001", written)
        self.assertIn("Checkup Notes: Patient is stable", written)

    @patch("os.path.exists", return_value=False)
    def test_csv_not_found(self, mock_exists):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            update_patient_checkup()
            self.assertIn("Patient details CSV file not found", fake_out.getvalue())

    @patch("builtins.input", side_effect=["P999"])
    @patch("pandas.read_csv")
    @patch("os.path.exists", return_value=True)
    def test_patient_not_found(self, mock_exists, mock_read_csv, mock_input):
        df = pd.DataFrame({
            "Patient_ID": ["P001"],
            "Name": ["Alice"],
            "Symptoms": ["Fever"]
        })
        mock_read_csv.return_value = df

        with patch("sys.stdout", new=StringIO()) as fake_out:
            update_patient_checkup()
            self.assertIn("Patient with ID 'P999' not found", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
