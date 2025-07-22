import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import pandas as pd

from Doctor_checkup import update_patient_checkup

class TestDoctorCheckup(unittest.TestCase):

    @patch("builtins.input", side_effect=["P001", "Patient is stable"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("pandas.read_csv")
    @patch("os.path.exists", return_value=True)
    def test_update_valid_patient(self, mock_exists, mock_read_csv, mock_file, mock_input):
        # Setup fake patient data
        df = pd.DataFrame({
            "Patient_ID": ["P001"],
            "Name": ["Alice"],
            "Symptoms": ["Fever"]
        })
        mock_read_csv.return_value = df

        with patch("sys.stdout", new=StringIO()) as fake_output:
            update_patient_checkup()
            output = fake_output.getvalue()

        # ✅ Use assert and assertEqual
        assert "Patient record updated" in output
        assertEqual = self.assertEqual  # alias
        assertEqual(mock_file.call_count > 0, True)

    @patch("os.path.exists", return_value=False)
    def test_csv_not_found(self, mock_exists):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            update_patient_checkup()
            output = fake_output.getvalue()

        # ✅ Use assert only
        assert "Patient details CSV file not found" in output

if __name__ == '__main__':
    unittest.main()
