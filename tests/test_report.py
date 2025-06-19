import json
import os
import tempfile
from unittest.mock import patch, mock_open
from typing import List
import pytest
from dataclasses import asdict

# Add src to path for imports
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from report import generate_report, print_report_to_console
from models.artwork import MuseumArtwork
from models.constituent import Constituent
from models.measurements import Measurement
from models.tag import Tag


class TestGenerateReport:
    """Test cases for the generate_report function."""

    def create_sample_artwork(self) -> MuseumArtwork:
        """Create a sample MuseumArtwork object for testing."""
        return MuseumArtwork(
            objectID=12345,
            isHighlight=True,
            accessionNumber="2023.1",
            accessionYear="2023",
            isPublicDomain=True,
            primaryImage="https://example.com/image.jpg",
            primaryImageSmall="https://example.com/small.jpg",
            additionalImages=[],
            constituents=[],
            department="Paintings",
            objectName="Painting",
            title="Test Artwork",
            culture="American",
            period="Modern",
            dynasty=None,
            reign=None,
            portfolio=None,
            artistRole="Artist",
            artistPrefix=None,
            artistDisplayName="Test Artist",
            artistDisplayBio="Test Bio",
            artistSuffix=None,
            artistAlphaSort="Artist, Test",
            artistNationality="American",
            artistBeginDate="1900",
            artistEndDate="1980",
            artistGender=None,
            artistWikidata_URL=None,
            artistULAN_URL=None,
            objectDate="1950",
            objectBeginDate=1950,
            objectEndDate=1950,
            medium="Oil on canvas",
            dimensions="24 x 36 in.",
            measurements=[],
            creditLine="Gift of Test Donor",
            geographyType=None,
            city=None,
            state=None,
            county=None,
            country=None,
            region=None,
            subregion=None,
            locale=None,
            locus=None,
            excavation=None,
            river=None,
            classification="Paintings",
            rightsAndReproduction=None,
            linkResource=None,
            metadataDate="2023-01-01",
            repository="Metropolitan Museum of Art",
            objectURL="https://www.metmuseum.org/art/collection/search/12345",
            tags=[],
            objectWikidata_URL=None,
            isTimelineWork=False,
            GalleryNumber="101"
        )

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_generate_report_single_artwork(self, mock_json_dump, mock_file):
        """Test generating report with a single artwork."""
        artwork = [self.create_sample_artwork()]
        
        generate_report(artwork)
        
        # Verify file was opened for writing
        mock_file.assert_called_once_with("report.json", "w")
        
        # Verify json.dump was called - it should be called with dictionaries, not the original objects
        assert mock_json_dump.call_count == 1
        call_args = mock_json_dump.call_args
        
        # Check that the first argument is a list of dictionaries
        dumped_data = call_args[0][0]
        assert isinstance(dumped_data, list)
        assert len(dumped_data) == 1
        assert isinstance(dumped_data[0], dict)
        assert dumped_data[0]["objectID"] == 12345
        assert dumped_data[0]["title"] == "Test Artwork"

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_generate_report_multiple_artworks(self, mock_json_dump, mock_file):
        """Test generating report with multiple artworks."""
        artwork1 = self.create_sample_artwork()
        artwork2 = self.create_sample_artwork()
        artwork2.objectID = 67890
        artwork2.title = "Second Test Artwork"
        
        artwork_list = [artwork1, artwork2]
        
        generate_report(artwork_list)
        
        # Verify file was opened for writing
        mock_file.assert_called_once_with("report.json", "w")
        
        # Verify json.dump was called with converted dictionaries
        assert mock_json_dump.call_count == 1
        call_args = mock_json_dump.call_args
        
        # Check that the first argument is a list of dictionaries
        dumped_data = call_args[0][0]
        assert isinstance(dumped_data, list)
        assert len(dumped_data) == 2
        assert isinstance(dumped_data[0], dict)
        assert isinstance(dumped_data[1], dict)
        assert dumped_data[0]["objectID"] == 12345
        assert dumped_data[1]["objectID"] == 67890
        assert dumped_data[1]["title"] == "Second Test Artwork"

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_generate_report_empty_list(self, mock_json_dump, mock_file):
        """Test generating report with an empty artwork list."""
        artwork_list = []
        
        generate_report(artwork_list)
        
        # Verify file was opened for writing
        mock_file.assert_called_once_with("report.json", "w")
        
        # Verify json.dump was called with empty list
        assert mock_json_dump.call_count == 1
        call_args = mock_json_dump.call_args
        dumped_data = call_args[0][0]
        assert isinstance(dumped_data, list)
        assert len(dumped_data) == 0

    @patch("builtins.open", side_effect=IOError("Permission denied"))
    def test_generate_report_file_error(self, mock_file):
        """Test that file I/O errors are properly raised."""
        artwork = [self.create_sample_artwork()]
        
        with pytest.raises(IOError, match="Permission denied"):
            generate_report(artwork)

    def test_generate_report_integration(self):
        """Integration test that actually writes and reads a file."""
        artwork = [self.create_sample_artwork()]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # Change to temp directory
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                generate_report(artwork)
                
                # Verify file was created
                assert os.path.exists("report.json")
                
                # Verify file contents
                with open("report.json", "r") as f:
                    data = json.load(f)
                
                assert len(data) == 1
                assert data[0]["objectID"] == 12345
                assert data[0]["title"] == "Test Artwork"
                
            finally:
                os.chdir(original_cwd)


class TestPrintReportToConsole:
    """Test cases for the print_report_to_console function."""

    def create_sample_artwork(self) -> MuseumArtwork:
        """Create a sample MuseumArtwork object for testing."""
        return MuseumArtwork(
            objectID=12345,
            isHighlight=True,
            accessionNumber="2023.1",
            accessionYear="2023",
            isPublicDomain=True,
            primaryImage="https://example.com/image.jpg",
            primaryImageSmall="https://example.com/small.jpg",
            additionalImages=[],
            constituents=[],
            department="Paintings",
            objectName="Painting",
            title="Test Artwork",
            culture="American",
            period="Modern",
            dynasty=None,
            reign=None,
            portfolio=None,
            artistRole="Artist",
            artistPrefix=None,
            artistDisplayName="Test Artist",
            artistDisplayBio="Test Bio",
            artistSuffix=None,
            artistAlphaSort="Artist, Test",
            artistNationality="American",
            artistBeginDate="1900",
            artistEndDate="1980",
            artistGender=None,
            artistWikidata_URL=None,
            artistULAN_URL=None,
            objectDate="1950",
            objectBeginDate=1950,
            objectEndDate=1950,
            medium="Oil on canvas",
            dimensions="24 x 36 in.",
            measurements=[],
            creditLine="Gift of Test Donor",
            geographyType=None,
            city=None,
            state=None,
            county=None,
            country=None,
            region=None,
            subregion=None,
            locale=None,
            locus=None,
            excavation=None,
            river=None,
            classification="Paintings",
            rightsAndReproduction=None,
            linkResource=None,
            metadataDate="2023-01-01",
            repository="Metropolitan Museum of Art",
            objectURL="https://www.metmuseum.org/art/collection/search/12345",
            tags=[],
            objectWikidata_URL=None,
            isTimelineWork=False,
            GalleryNumber="101"
        )

    @patch("builtins.print")
    def test_print_report_single_artwork(self, mock_print):
        """Test printing report with a single artwork."""
        artwork = [self.create_sample_artwork()]
        outdir = "/test/output"
        
        print_report_to_console(artwork, outdir)
        
        # Verify print was called 3 times
        assert mock_print.call_count == 3
        
        # Get all the printed content
        printed_calls = [call.args[0] for call in mock_print.call_args_list]
        
        # Check the content of each call
        assert "Downloaded the following pieces:" in printed_calls[0]
        assert "Test Artwork" in printed_calls[1] and "Test Artist" in printed_calls[1]
        assert "Saved artwork to: /test/output" in printed_calls[2]

    @patch("builtins.print")
    def test_print_report_multiple_artworks(self, mock_print):
        """Test printing report with multiple artworks."""
        artwork1 = self.create_sample_artwork()
        artwork2 = self.create_sample_artwork()
        artwork2.objectID = 67890
        artwork2.title = "Second Test Artwork"
        artwork2.artistDisplayName = "Second Artist"
        
        artwork_list = [artwork1, artwork2]
        outdir = "/test/output"
        
        print_report_to_console(artwork_list, outdir)
        
        # Should print header, two artwork lines, and footer
        assert mock_print.call_count == 4
        
        # Check that both artworks are mentioned
        all_calls = [str(call) for call in mock_print.call_args_list]
        combined_output = " ".join(all_calls)
        
        assert "Test Artwork" in combined_output
        assert "Second Test Artwork" in combined_output
        assert "Test Artist" in combined_output
        assert "Second Artist" in combined_output

    @patch("builtins.print")
    def test_print_report_empty_list(self, mock_print):
        """Test printing report with an empty artwork list."""
        artwork_list = []
        outdir = "/test/output"
        
        print_report_to_console(artwork_list, outdir)
        
        # Should print header and footer only
        assert mock_print.call_count == 2
        
        # Verify the calls
        mock_print.assert_any_call("Downloaded the following pieces:\n")
        mock_print.assert_any_call("\nSaved artwork to: /test/output")

    @patch("builtins.print")
    def test_print_report_unknown_artist(self, mock_print):
        """Test printing report with artwork that has no artist name."""
        artwork = self.create_sample_artwork()
        artwork.artistDisplayName = ""  # Empty artist name
        
        artwork_list = [artwork]
        outdir = "/test/output"
        
        print_report_to_console(artwork_list, outdir)
        
        # Check that "Unknown artist" appears in the output
        all_calls = [str(call) for call in mock_print.call_args_list]
        combined_output = " ".join(all_calls)
        
        assert "Unknown artist" in combined_output

    @patch("builtins.print")
    def test_print_report_special_characters_in_outdir(self, mock_print):
        """Test printing report with special characters in output directory."""
        artwork = [self.create_sample_artwork()]
        outdir = "/test/output with spaces & symbols!"
        
        print_report_to_console(artwork, outdir)
        
        # Verify the output directory is printed correctly
        mock_print.assert_any_call("\nSaved artwork to: /test/output with spaces & symbols!")
