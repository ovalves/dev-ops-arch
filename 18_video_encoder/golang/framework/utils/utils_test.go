package utils_test

import (
	"encoder/framework/utils"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsJson(t *testing.T) {
	json := `{
  				"id": "525b5fd9-700d-4feb-89c0-415a1e6e148c",
  				"file_path": "file_example_MP4_480_1_5MG.mp4",
  				"status": "pending"
			}`

	err := utils.IsJson(json)
	require.Nil(t, err)

	json = `file_example_MP4_480_1_5MG`
	err = utils.IsJson(json)
	require.Error(t, err)
}
